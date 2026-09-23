import argparse

from .app import process_shot
from .config import load_config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspresso espresso shot analyzer prototype"
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Run using manually supplied measurements.",
    )
    parser.add_argument("--mass", type=float, help="Final espresso mass in grams")
    parser.add_argument("--time", type=float, help="Extraction time in seconds")
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="Optional measured temperature in Celsius",
    )
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to configuration JSON file",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not append this shot to CSV history",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if not args.simulate:
        raise SystemExit(
            "Hardware mode is not implemented yet. Use --simulate while the "
            "sensor drivers are under development."
        )

    if args.mass is None or args.time is None:
        raise SystemExit("Simulation mode requires --mass and --time.")

    config = load_config(args.config)
    shot, result = process_shot(
        mass_g=args.mass,
        extraction_time_s=args.time,
        temperature_c=args.temperature,
        config=config,
        save_history=not args.no_save,
    )

    print("\nInspresso Shot Result")
    print(f"Mass: {shot.mass_g:.1f} g")
    print(f"Time: {shot.extraction_time_s:.1f} s")
    if shot.temperature_c is not None:
        print(f"Temperature: {shot.temperature_c:.1f} C")
    print(f"Classification: {result.classification}")
    print(f"Recommendation: {result.recommendation}")


if __name__ == "__main__":
    main()

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


console = Console()


def show_banner():
    banner = Table.grid(expand=False)
    banner.add_column(justify="center")
    banner.add_row(Text("NEARBY FLIGHTS", style="bold white"))
    banner.add_row(Text("Aircraft near airports, cities, or coordinates", style="bright_black"))

    console.print(
        Align.center(
            Panel.fit(
                banner,
                title="[cyan]ADS-B[/cyan]",
                border_style="bright_black",
                padding=(1, 4),
            )
        )
    )


def show_menu():
    menu = Table.grid(expand=False, padding=(0, 4))
    menu.add_column(justify="left")
    menu.add_column(justify="left")
    menu.add_column(justify="left")
    menu.add_column(justify="left")
    menu.add_row(
        "[bold cyan][1][/bold cyan] Airport",
        "[bold cyan][2][/bold cyan] City",
        "[bold cyan][3][/bold cyan] Coordinates",
        "[bold cyan][4][/bold cyan] Exit",
    )

    console.print()
    console.print(
        Align.center(
            Panel.fit(menu, title="Menu", border_style="bright_black", box=box.ROUNDED)
        )
    )


def show_coordinate_help():
    details = Table.grid(padding=(0, 2))
    details.add_column(style="bright_black")
    details.add_column(style="white")
    details.add_row("Format", "Decimal degrees, using a dot")
    details.add_row("Latitude", "-90 to 90, example: -23.4356")
    details.add_row("Longitude", "-180 to 180, example: -46.4731")
    details.add_row("Tip", "South and West use negative numbers")

    console.print()
    console.print(
        Panel(
            details,
            title="[bold]Custom Coordinates[/bold]",
            border_style="cyan",
            box=box.ROUNDED,
        )
    )


def show_location(location):
    details = Table.grid(padding=(0, 3))
    details.add_column(style="bright_black")
    details.add_column(style="white")
    details.add_row("Latitude", format_number(location["lat"], 4))
    details.add_row("Longitude", format_number(location["lon"], 4))
    details.add_row("Radius", f"{format_number(location['radius_nm'])} nm")

    console.print()
    console.print(
        Panel(
            details,
            title=f"[bold]{location['name']}[/bold]",
            border_style="cyan",
            box=box.ROUNDED,
        )
    )


def show_aircraft_table(aircraft_list):
    table = Table(
        title="Nearby Aircraft",
        caption="Alt m | Speed km/h | Distance km | V/S vertical speed",
        box=box.SIMPLE_HEAVY,
        header_style="bold cyan",
        title_style="bold",
        caption_style="bright_black",
        show_lines=False,
    )
    table.add_column("Flight", style="bold white", no_wrap=True, max_width=8)
    table.add_column("Type", style="magenta", no_wrap=True, max_width=4)
    table.add_column("Reg", style="blue", no_wrap=True, max_width=7)
    table.add_column("Alt m", justify="right", no_wrap=True)
    table.add_column("Spd", justify="right", no_wrap=True)
    table.add_column("V/S", justify="right", no_wrap=True)
    table.add_column("Dist", justify="right", no_wrap=True)
    table.add_column("Seen", justify="right", no_wrap=True)

    for aircraft in sorted(aircraft_list, key=distance_sort_key):
        table.add_row(
            format_value(aircraft["flight"]),
            format_value(aircraft["type"]),
            format_value(aircraft["reg"]),
            format_number_value(aircraft["altitude_m"]),
            format_number_value(aircraft["speed_kmh"]),
            format_vertical_rate(aircraft["vertical_rate"]),
            format_number_value(aircraft["distance_km"], decimals=1),
            format_seen(aircraft["seen"]),
        )

    console.print()
    console.print(Align.center(table))


def show_error(message):
    console.print(f"\n[bold red]Error:[/bold red] {message}")


def show_warning(message):
    console.print(f"\n[bold yellow]Warning:[/bold yellow] {message}")


def show_goodbye():
    console.print("\n[cyan]Goodbye.[/cyan]")


def fetch_status(location):
    return console.status(
        f"[cyan]Querying ADS-B data near {location['name']}...[/cyan]",
        spinner="dots",
    )


def distance_sort_key(aircraft):
    distance = aircraft["distance_km"]
    if distance is None:
        return float("inf")
    return distance


def format_value(value):
    if value is None or value == "":
        return "[bright_black]N/A[/bright_black]"

    return str(value)


def format_number_value(value, decimals=0):
    if value is None:
        return "[bright_black]N/A[/bright_black]"

    return format_number(value, decimals)


def format_number(value, decimals=0):
    if decimals == 0:
        return f"{round(value):,}"

    return f"{value:,.{decimals}f}"


def format_seen(seen):
    if seen is None:
        return "[bright_black]N/A[/bright_black]"

    style = "green" if seen <= 10 else "yellow" if seen <= 30 else "red"
    return f"[{style}]{seen:.1f}s[/{style}]"


def format_vertical_rate(rate):
    if rate is None:
        return "[bright_black]N/A[/bright_black]"

    if rate > 0:
        return f"[green]↑{format_number(rate)}[/green]"

    if rate < 0:
        return f"[red]↓{format_number(abs(rate))}[/red]"

    return "[bright_black]level[/bright_black]"

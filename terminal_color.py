def print_colored_text():
    colors = {
        'black': '0;30',
        'dark_gray': '1;30',
        'red': '0;31',
        'light_red': '1;31',
        'green': '0;32',
        'light_green': '1;32',
        'brown_orange': '0;33',
        'yellow': '1;33',
        'blue': '0;34',
        'light_blue': '1;34',
        'purple': '0;35',
        'light_purple': '1;35',
        'cyan': '0;36',
        'light_cyan': '1;36',
        'light_gray': '0;37',
        'white': '1;37',
    }

    backgrounds = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'light_gray': '47',
    }

    for color_name, color_code in colors.items():
        for bg_name, bg_code in backgrounds.items():
            print(f"\033[{color_code};{bg_code}mThis is {color_name} text on a {bg_name} background! (Foreground: {color_code}, Background: {bg_code})\033[0m")

    print("\033[5;31;42mText\033[0m -> verbatim: \\033[0;31;42mText\\033[0m " )
    print("  \\033[ -- Start sequence" )
    print("  0; -- formatting 0-normal, 1-bold, 3-italic, 4-underline, 5-blink" )
    print("  31; -- foreground color" )
    print("  42 -- background color" )
    print("  \\033[0m -- Reset sequence" )
    print("! to test in bash use echo -e String" )

if __name__ == "__main__":
    print_colored_text()

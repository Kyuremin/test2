import time


def countdown(minutes):
    """Count down for the given minutes."""
    seconds = int(minutes * 60)
    if seconds <= 0:
        return
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print()


def main():
    try:
        work = float(input("Çalışma süresi (dakika): "))
        short_break = float(input("Mola süresi (dakika): "))
        repeats = int(input("Ka\u00e7 d\u00f6ng\u00fc tekrarlans\u0131n?: "))
    except ValueError:
        print("Ge\u00e7ersiz giri\u015f yap\u0131ld\u0131. L\u00fctfen say\u0131 girin.")
        return

    for i in range(1, repeats + 1):
        print(f"#{i}. Pomodoro ba\u015flad\u0131! {work} dakika \u00e7al\u0131\u015f.")
        countdown(work)
        if i < repeats:
            print(f"Mola zaman\u0131! {short_break} dakika mola ver.")
            countdown(short_break)
    print("T\u00fcm pomodorolar tamamland\u0131. Tebrikler!")


if __name__ == "__main__":
    main()

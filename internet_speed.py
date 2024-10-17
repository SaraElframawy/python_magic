import speedtest

def speed_test():
    test = speedtest.Speedtest()
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    ping = test.results.ping
    print("Download speed:", down_speed, "Mbps")
    print("Upload speed:", up_speed, "Mbps")
    print("Ping:", ping, "ms")

speed_test()

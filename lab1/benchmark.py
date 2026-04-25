import urllib.request, time, statistics

times = []
for i in range(100):
    start = time.time()
    urllib.request.urlopen("http://localhost:5000/")
    times.append((time.time() - start) * 1000)
    print(f"Request {i+1}: {times[-1]:.0f}ms")

times.sort()
print(f"\n50th percentile: {times[49]:.0f}ms")
print(f"90th percentile: {times[89]:.0f}ms")
print(f"99th percentile: {times[98]:.0f}ms")
print(f"100th (max):     {times[-1]:.0f}ms")
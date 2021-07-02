# 행복한지 슬픈지
import sys
s = sys.stdin.readline().rstrip()

hap = s.count(":-)")
sad = s.count(":-(")

if not hap and not sad: print("none")
elif hap == sad: print("unsure")
elif hap > sad: print("happy")
elif hap < sad: print("sad")
duration = 0
cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())

pinkBin = int(input())

pinkBin -= (du+dd+dp)

while(pinkBin > 0):
    duration += 1
    if duration % cu == 0:
        pinkBin -= du
    if duration % cd == 0:
        pinkBin -= dd
    if duration % cp == 0:
        pinkBin -= dp
print(duration)
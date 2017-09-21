# https://www.reddit.com/r/dailyprogrammer/comments/71gbqj/20170920_challenge_332_intermediate_training_for/

peaks = list(map(int, input().split()))

path = [peaks.pop(0)]
higherpeaks = []

for index, peak in enumerate(peaks):
    higherpeaks.append((peak, sum(1 for p in peaks[index+1:] if p > peak)))
    
for index, peak in enumerate(peaks):
    if index+1 < len(peaks):
        p = higherpeaks[index][1]
        highestpeaks = [hp[1] for hp in higherpeaks[index+1:] if hp[0] > path[-1]]
        if peak > path[-1] and p > max(highestpeaks):
            path.append(peak)
    elif peak > path[-1]:
        path.append(peak)

print(path)
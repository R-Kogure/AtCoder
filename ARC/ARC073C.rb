N,T = gets.split.map(&:to_i)
t = gets.split.map(&:to_i)
ans = T

(N - 1).times do |i|
    ans += [t[i + 1] - t[i], T].min
end

p ans

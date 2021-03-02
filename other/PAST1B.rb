def gaps(arr)
  arr.length.times do |i|
    next if i == 0
    gap = arr[i].to_i - arr[i - 1].to_i
    if gap == 0
      puts 'stay'
    elsif gap > 0
      puts "up #{gap.abs}"
    elsif gap < 0
      puts "down #{gap.abs}"
    end
  end
end
array = []
days = gets
days.to_i.times do |i|
  array << gets
end
gaps(array)

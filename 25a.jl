function base_10(s::String)::Int
	t = reverse(s)
	answer = 0
	for i in eachindex(t)
		answer += (findfirst(t[i], "=-012")[1] - 3) * 5 ^ (i - 1)
	end
	return answer
end

function normal_base_5(x::Int)::Array
	answer = []
	while x > 0
		append!(answer, x % 5)
		x ÷= 5
	end
	return answer
end

function wackify!(normal::Array)::Nothing
	N = length(normal)
	for i in 1:N
		if normal[i] ≥ 5
			if i == N
				append!(normal, normal[i] ÷ 5)
			else
				normal[i + 1] += normal[i] ÷ 5
			end
			normal[i] %= 5
		end
		if normal[i] ≤ 2
			continue
		else
			if i == N
				append!(normal, 1)
			else
				normal[i + 1] += 1
			end
			normal[i] -= 5
		end
	end
end

total = 0
for _ in 1:113
	num = readline()
	global total += base_10(num)
end

normal = normal_base_5(total)
wackify!(normal)

answer = ""
for c in normal
	global answer *= "=-012"[c + 3]
end
println(reverse(answer))

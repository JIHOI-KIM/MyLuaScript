-- All global variables, modules should be listed in _G

function remove(tb, ind)
	local last = #tb
	tb[ind] = tb[last]
	tb[last] = nil
end

function printT(tb, title)
	if tb == nil then return end
	if #tb == 0 then return end
	print("-------------------------------")
	print(string.format("[TYPE: %s]",title))
	local i = 0
	for k, v in pairs(tb) do
		io.write(string.format("[%-25s] ",v.name and v.name or v))
		i = i+1
		if i == 4 then print(); i=0 end
	end
	print()
	print("-------------------------------")
end

local tables = {}

local funcList = {}
local numberList = {}
local booleanList = {}
local stringList = {}
local userdataList = {}
local threadList = {}
local nilList = {}

local done = {}
tables[1] = {val = _G, name=nil}
done[1] = {val = _G, name=nil}

for i, tb in ipairs(tables) do
	for k, v in pairs(tb.val) do
		if type(v) == "function" then funcList[#funcList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "number" then numberList[#numberList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "string" then stringList[#stringList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "boolean" then booleanList[#booleanList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "userdata" then userdataList[#userdataList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "thread" then threadList[#threadList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "nil" then nilList[#nilList+1] = tb.name and tb.name .."." .. k or k
		elseif type(v) == "table" then
			local doneFlag = true
			for _, donev in pairs(done) do
				if v == donev then
					doneFlag = false
					break
				end
			end
			if doneFlag then
				tables[#tables+1] = {val = v, name = tb.name and tb.name .."." .. k or k}
				done[#done+1] = {val = v, name = tb.name and tb.name .."." .. k or k}
			end
		end
	end
	remove(tables, i)
end

print("STATISTIC")
print("-------------------------------")
print(string.format("%-10s: %-10d ","table", #done))
print(string.format("%-10s: %-10d ","function", #funcList))
print(string.format("%-10s: %-10d ","number", #numberList))
print(string.format("%-10s: %-10d ","string", #stringList))
print(string.format("%-10s: %-10d ","boolean", #booleanList))
print(string.format("%-10s: %-10d ","userdata", #userdataList))
print(string.format("%-10s: %-10d ","thread", #threadList))
print(string.format("%-10s: %-10d ","nil", #nilList))

for i,v in ipairs(done) do
	if v == _G then
		done[i].name="_G"
		break
	end
end
		
printT(done, "TABLE")
printT(funcList, "FUNCTION")
printT(numberList, "NUMBER")
printT(stringList, "STRING")
printT(booleanList, "BOOLEAN")
printT(userdataList, "USERDATA")
printT(threadList, "THREADLIST")
printT(nilList, "NIL")



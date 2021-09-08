-- All global variables, modules should be listed in _G

local i = 0
for k, v in pairs(_G) do
	io.write(string.format("[%-15s | %-15s] ",k,type(v)))
	i = i+1
	if i == 3 then print(); i=0 end
end
print()

print("AFTER DEFINE GLOBAL VARIABLE ZZZ = 'this is global variable' ")
print("AFTER DEFINE GLOBAL VARIABLE local YYY = 'this is local variable'\n")
ZZZ = 'this is global variable'
local YYY = 'this is local variable'

local i = 0
for k, v in pairs(_G) do
	io.write(string.format("[%-15s | %-15s] ",k,type(v)))
	i = i+1
	if i == 3 then print(); i=0 end
end
print()

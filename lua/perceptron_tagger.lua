local json = require("json")

local PerceptronTagger = {}

PerceptronTagger.__index = PerceptronTagger

function PerceptronTagger:new()
	local obj = {
		weights = {},
		classes = {},
		START = { "-START-", "-START2-" },
		END = { "-END-", "-END2-" },
	}
	setmetatable(obj, PerceptronTagger)
	return obj
end

function PerceptronTAgger:load(json_path)
	local file = io.open(json_path, "r")
	if not file then
		error("Not such file: " .. json_path)
	end
	local content = file:read("*all")
	file:close()

	local model = json.decode(content)
	self.weights = model.weights
	self.classes = model.classes

	print(string.format("Modelo con %d pesos y %d tags", self:count_table(self.weights), #self.classes))
end

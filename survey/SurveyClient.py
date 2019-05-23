from SurveyAnalysis import Analysis
import json

f = open("input.json", "r")
input_str = f.read()
analysis = Analysis(input_str)

result = analysis.drop_question_groups(["Rando"]).math("average_answers").digest()
print(json.dumps(result, indent=4, sort_keys=True))

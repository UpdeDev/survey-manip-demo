from SurveyAnalysis import Analysis

f = open("input.json", "r")
input_str = f.read()
analysis = Analysis(input_str)

result = analysis.filter(["answers.length > 1"]).math(["qlabel=vq5_4Rank", "qlabel=otherquestion"], "sum").digest()

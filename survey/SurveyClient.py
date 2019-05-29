from SurveyAnalysis import Analysis
import json
import SurveyAnalysis

f = open("input.json", "r")
input_str = f.read()
analysis = Analysis(input_str)

dump = analysis\
.drop_question_groups(["Rando"])\
.math("average_answers")\
.math("std_dev_answers")\
.dump()
f.close()

outfile = open("dump.json", "w+")
outfile.write(json.dumps(dump))
outfile.close() 

infile = open("dump.json", "r")
queue = json.loads(infile.read())
analysis = Analysis(input_str, SurveyAnalysis.extract_queue(queue))

result = analysis.digest()
print(result)

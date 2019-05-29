from Link.LinkModule import Link
import math

class MathLink(Link):

    def _extract_answers(self, survey):
        question_groups = survey["questionGroup"]
        answer_values = []
        for group_id in question_groups:
            cur_group = question_groups[group_id]
            questions = cur_group["questions"]
            for question_id in questions:
                cur_question = questions[question_id]
                answers = cur_question["answers"]
                for answer_id in answers:
                    answer_values.append(int(answers[answer_id]))
        return answer_values

    def _average(self, values):
        sum = 0
        for value in values:
            sum = sum + value
        return sum / len(values)

    def _average_answers(self, survey):
        answers = self._extract_answers(survey)
        if len(answers) == 0:
            return 0
        survey["answer_average"] = self._average(answers)
        return survey

    def _std_dev_answers(self, survey):
        answers = self._extract_answers(survey)
        if len(answers) == 0:
            return 0
        mean = self._average(answers)
        sum_of_squares = 0
        for answer in answers:
            delta = answer - mean
            square = delta * delta
            sum_of_squares = sum_of_squares + square
        variance = sum_of_squares / len(answers)
        survey["answer_std_dev"] = math.sqrt(variance)
        return survey

    def _process(self, survey):
        operation_switch = {
            "average_answers": self._average_answers,
            "std_dev_answers": self._std_dev_answers
        }
        opfunc = operation_switch.get(self.operation)
        if(opfunc == None):
            raise ValueError

        response = opfunc(survey)
        return response

    def _dump(self):
        return {'type': 'MathLink', 'operation': self.operation}

    def __init__(self, operation):
        self.operation = operation

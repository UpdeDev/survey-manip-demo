from Link.LinkModule import Link

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

    def _average_answers(self, survey):
        answers = self._extract_answers(survey)
        if len(answers) == 0:
            return 0
        sum = 0
        for answer in answers:
            sum = sum + answer
        survey["answer_average"] = sum / len(answers)
        return survey

    def _process(self, survey):
        operation_switch = {
            "average_answers": self._average_answers
        }
        opfunc = operation_switch.get(self.operation)
        if(opfunc == None):
            raise ValueError

        response = opfunc(survey)
        return response

    def __init__(self, operation):
        self.operation = operation

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Separate letter-logs from digit-logs: each in their own list
        letter_logs = []
        digit_logs = []

        for log in logs:
            splitted_log = log.split()
            if splitted_log[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        # Sort letter-logs
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # Concatenate letter-logs and digit-logs
        result_logs = letter_logs + digit_logs

        return result_logs


        

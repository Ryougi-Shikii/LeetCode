class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, action, ts_str = log.split(':')
            fn_id = int(fn_id_str)
            timestamp = int(ts_str)

            if action == 'start':
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                curr_fn = stack.pop()
                res[curr_fn] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res
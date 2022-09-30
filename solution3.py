import itertools
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    users = [list(map(int, input().split())) for _ in range(7)]
    emoticons = list(map(int, input().split()))

    discount_ratio = {
        10: lambda x: x * 0.9,
        20: lambda x: x * 0.8,
        30: lambda x: x * 0.7,
        40: lambda x: x * 0.6,
    }

    # print(list(itertools.product(*[[10, 20, 30, 40] for _ in range(len(emoticons))])))
    # [(10, 10), (10, 20), (10, 30), (10, 40), (20, 10), (20, 20), (20, 30), (20, 40), (30, 10), (30, 20), (30, 30), (30, 40), (40, 10), (40, 20), (40, 30), (40, 40)]
    emoticon_ratios = itertools.product(*[[10, 20, 30, 40] for _ in range(len(emoticons))])
    # emoticon_ratios = [list(itertools.product(*[[10, 20, 30, 40] for _ in range(len(emoticons))]))[-1]]

    max_join_count = float('-inf')
    max_join_sum = float('-inf')
    curr_ratio = 0
    for e_ratio in emoticon_ratios:
        # print(e_ratio) # (10, 10)
        e_ratio_and_discount_price = []  # [(10, 6300.0), (10, 8100.0)]
        for price, ratio in zip(emoticons, e_ratio):
            # e_ratio_and_discount_price.append((ratio, discount_ratio[ratio](price))
            e_ratio_and_discount_price.append((ratio, discount_ratio[ratio](price), price))

        join_count = 0
        no_join_sum = 0
        for user in users:
            b_ratio, b_price = user
            # print(b_ratio, b_price)

            p_sum = 0
            for ratio, d_price, price in e_ratio_and_discount_price:
                if ratio >= b_ratio:
                    p_sum += d_price

            if p_sum >= b_price:
                join_count += 1
                p_sum = 0
            else:
                no_join_sum += p_sum

        if join_count == max_join_count:
            # print(max_join_count, max_join_sum)
            if no_join_sum > max_join_sum:
                max_join_sum = no_join_sum

        elif join_count > max_join_count:
            # print(join_count, no_join_sum)
            max_join_count = join_count
            max_join_sum = no_join_sum
            curr_ratio = e_ratio

        # if e_ratio == (40, 40, 20, 40):
        #     print("asdf")
        #     print(join_count)
        #     print(no_join_sum)
        #     print(e_ratio)
        # 3
        # 19760.0
        # (40, 40, 20, 40)

    print([max_join_count, int(max_join_sum), e_ratio])
    # return [max_join_count, int(max_join_sum)]

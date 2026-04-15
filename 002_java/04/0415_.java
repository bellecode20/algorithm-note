# 프로그래머스 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=java
import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        // int[]끼리 자동 비교 못해서 우선순위 정렬 기준 지정
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0]; // 길이 짧은 순
            return a[1] - b[1];                   // 시작 인덱스 작은 순
        });

        int n = sequence.length;
        int left = 0;
        int right = 0;
        int sum = sequence[left];

        while (left <= right) {
            if (sum == k) {
                pq.offer(new int[]{right - left, left, right});

                sum -= sequence[left];
                left++;
            } else if (sum < k) {
                if (right + 1 >= n) {
                    break;
                }

                right++;
                sum += sequence[right];
            } else {
                sum -= sequence[left];
                left++;
            }
        }

        int[] result = pq.poll();

        return new int[]{result[1], result[2]};
    }
}

class SolutionVersion2 {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;

        int left = 0;
        int right = 0;
        int sum = sequence[0];

        int bestLeft = 0;
        int bestRight = n - 1;
        int bestLength = n;

        while (left <= right) {
            if (sum == k) {
                int currentLength = right - left;

                if (currentLength < bestLength) {
                    bestLength = currentLength;
                    bestLeft = left;
                    bestRight = right;
                }

                sum -= sequence[left];
                left++;
            } else if (sum < k) {
                if (right + 1 >= n) break;

                right++;
                sum += sequence[right];
            } else {
                sum -= sequence[left];
                left++;
            }
        }

        return new int[]{bestLeft, bestRight};
    }
}
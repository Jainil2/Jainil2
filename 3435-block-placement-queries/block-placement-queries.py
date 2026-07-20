class Solution:
    def __init__(self):
        self.max_coordinate = 50000
        self.segment_tree = []
        self.obstacles = SortedList()

    def update_segment_tree(
        self,
        position: int,
        value: int,
        node: int,
        left_bound: int,
        right_bound: int,
    ) -> None:
        if left_bound == right_bound:
            self.segment_tree[node] = value
            return

        mid = (left_bound + right_bound) // 2

        if position <= mid:
            self.update_segment_tree(
                position,
                value,
                2 * node,
                left_bound,
                mid,
            )
        else:
            self.update_segment_tree(
                position,
                value,
                2 * node + 1,
                mid + 1,
                right_bound,
            )

        self.segment_tree[node] = max(
            self.segment_tree[2 * node],
            self.segment_tree[2 * node + 1],
        )

    def query_segment_tree(
        self,
        query_left: int,
        query_right: int,
        node: int,
        left_bound: int,
        right_bound: int,
    ) -> int:
        if query_left <= left_bound and right_bound <= query_right:
            return self.segment_tree[node]

        mid = (left_bound + right_bound) // 2
        maximum_gap = 0

        if query_left <= mid:
            maximum_gap = max(
                maximum_gap,
                self.query_segment_tree(
                    query_left,
                    query_right,
                    2 * node,
                    left_bound,
                    mid,
                ),
            )

        if query_right > mid:
            maximum_gap = max(
                maximum_gap,
                self.query_segment_tree(
                    query_left,
                    query_right,
                    2 * node + 1,
                    mid + 1,
                    right_bound,
                ),
            )

        return maximum_gap

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        self.segment_tree = [0] * (4 * self.max_coordinate)
        self.obstacles = SortedList([0, self.max_coordinate])

        self.update_segment_tree(
            self.max_coordinate,
            self.max_coordinate,
            1,
            0,
            self.max_coordinate,
        )

        results = []

        for query in queries:
            if query[0] == 1:
                obstacle_position = query[1]

                right_obstacle_index = min(
                    len(self.obstacles) - 1,
                    self.obstacles.bisect_right(obstacle_position),
                )

                right_obstacle = self.obstacles[right_obstacle_index]
                left_obstacle = self.obstacles[right_obstacle_index - 1]

                self.update_segment_tree(
                    obstacle_position,
                    obstacle_position - left_obstacle,
                    1,
                    0,
                    self.max_coordinate,
                )

                self.update_segment_tree(
                    right_obstacle,
                    right_obstacle - obstacle_position,
                    1,
                    0,
                    self.max_coordinate,
                )

                self.obstacles.add(obstacle_position)

            else:
                right_obstacle_index = min(
                    len(self.obstacles) - 1,
                    self.obstacles.bisect_right(query[1]),
                )

                previous_obstacle = self.obstacles[right_obstacle_index - 1]

                last_interval = query[1] - previous_obstacle

                maximum_completed_interval = self.query_segment_tree(
                    0,
                    previous_obstacle,
                    1,
                    0,
                    self.max_coordinate,
                )

                maximum_available_interval = max(
                    last_interval,
                    maximum_completed_interval,
                )

                results.append(maximum_available_interval >= query[2])

        return results
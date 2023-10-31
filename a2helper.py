################################################################################
# Part 1 - Querying the data
################################################################################
def find_bridge_by_id(bridges: list[list], bridge_id: int) -> list:
    """
    从桥梁列表中查找指定ID的桥梁并返回其数据。
    """
    # hit: 遍历bridges列表 检查所有的桥梁中里面有没有和bridge_id一样的id，
    # 如果有 那么返回桥梁的数据。如果没有 那么返回一个空列表 也就是 []


def find_bridges_in_radius(bridges: list[list], lat: float, lon: float,
                           radius: int, exclusions: list[int]) -> list[int]:
    """
    返回位于给定经纬度半径内的桥梁的ID。
    """
    # hit: 首先你需要判定这个桥梁是否不在 ‘ exclusions ’ 里
    # 可以用calculate_distance来计算距离
    # 如果这个距离小于radius 那么这就是一个在半径内的桥梁


def get_bridge_condition(bridges: list[list], bridge_id: int) -> float:
    """
    返回指定ID的桥梁的最近的BCI分数。
    """
    # hit: 使用find_bridge_by_id
    # 你不需要关心years 你只需要找scores里面最靠前并且非 MISSING_BCI 的数字


def calculate_average_condition(bridge: list, start: int, stop: int) -> float:
    """
    返回在指定开始和结束年份之间的桥梁的平均BCI分数。
    """
    # hit : 一座桥的COLUMN_BCI里的INDEX_BCI_YEARS是存储的所有年份
    #       一座桥的COLUMN_BCI里的INDEX_BCI_SCORES是存储的所有年份
    #       所有的year和scores是一一对应的 which means 只要year 
    #       pass 那么相同index的scores就是你可以用的


################################################################################
# Part 2 - Mutating the data
################################################################################
def inspect_bridge(bridges: list[list], bridge_id: int, inspect_date: str,
                   inspect_bci: float) -> None:
    """
    根据最新的检查日期和BCI分数更新指定ID的桥梁数据。
    
    :param bridges: 桥梁数据的列表，每个桥梁的数据也是一个列表。
    :param bridge_id: 需要更新的桥梁的ID。
    :param inspect_date: 桥梁的最新检查日期，格式为'MM/DD/YYYY'。
    :param inspect_bci: 在inspect_date指定的年份中的桥梁的最新BCI分数。
    """

    #  不要使用calculate_distance来寻找正确桥梁 因为指针会不一样
    #  从inspect_date中提取年份 也就是最后四位数
    #  注意 这是更新的东西 所以不管在years里 还是在scores里都是应该加在list的开头


def rehabilitate_bridge(bridges: list[list], bridge_ids: list[int],
                        new_year: str, is_major: bool) -> None:
     """
    更新在bridge_ids中指定ID的桥梁的最后修复日期。

    :param bridges: 桥梁数据的列表，每个桥梁的数据也是一个列表。
    :param bridge_ids: 需要更新的桥梁的ID列表。
    :param new_year: 新的修复日期。
    :param is_major: True:则更新主要修复日期 False:更新次要修复日期。
    """
    #同样 不要使用calculate_distance来寻找正确桥梁 因为指针会不一样


################################################################################
# Part 3 - Implementing useful algorithms
################################################################################
def find_worst_bci(bridges: list[list], bridge_ids: list[int]) -> int:
    """
    返回在bridge_ids中拥有最低最新BCI分数的桥梁的ID。
    
    如果存在多个桥梁具有相同的最低BCI分数,则返回ID较小的那个桥梁。
    
    :param bridges: 桥梁数据的列表，每个桥梁的数据也是一个列表。
    :param bridge_ids: 需要检查的桥梁的ID列表。
    """
    #   假设第一个桥梁ID为当前最差的桥梁,并获取其BCI分数。
    #   对于每个ID,使用`get_bridge_condition`function获取其最新的BCI分数
    #   也就是使用 get_bridge_condition 。
    #   一个个比较所有的桥梁的bci然后找出最低的
    #   sort()会有用


def map_route(bridges: list[list], lat: float, lon: float,
              max_bridges: int, radius: int) -> list[int]:
    """
    这个有点难 做好心理准备

    根据给定的起始位置、桥梁列表、最大桥梁数和半径，为桥梁绘制一条路径。

    Parameters:
    - bridges: 桥梁的列表。
    - lat: 起始纬度。
    - lon: 起始经度。
    - max_bridges: 路径上的最大桥梁数量。
    - radius: 查找桥梁的半径。

    Returns:
    - route: 桥梁ID的列表,表示要遍历的路径。

    为了大家更好的理解 我来讲个小故事：
        你是一个管理员 你一开始站在lat lon的这个点 然后你像四周看去(radius)
        看到了5座桥梁(打比方) 然后你找出了这里面最低bci的一个桥梁 然后走了过去
        走到这个桥梁后 你拿出小本子记录下了这个桥梁的id
        
        然后你现在站在哪呢? 就是这个桥的lat和lon对吧 然后你用你现在的lat和lon
        再向四周看去 然后.......

        最后你获得了你走过的路线 也就是我们的这个小本子 这就是你要返回的东西

    """

################################################################################
# Part 4 - Reading and cleaning raw data
################################################################################


def clean_length_data(raw_length: str) -> float:
    """
    这个很简单 自己想
    """


def trim_from_end(raw_data: list, count: int) -> None:
    """
    这个也很简单 自己想
    """


def clean_span_data(raw_spans: str) -> list[float]:
    """
    返回来自raw_spans的跨度长度列,其顺序与raw_spans中的顺序相同。
    
    :param raw_spans: 原始的跨度数据,其格式在“Bridge Spans”部分中有描述。
    """

    # hit:所有的东西都在 ‘=’ 和 ‘；’中间 可以去学一下split
    


def clean_bci_data(bci_years: list[str], start_year: int, bci_scores: list) -> \
        None:
    """
    这个也很简单 year里填start year 然后递减 scores里填将''替换为MISSING_BCI
    """
    

#恭喜你写完了 现在请来加我微信我想扩列：1224917119

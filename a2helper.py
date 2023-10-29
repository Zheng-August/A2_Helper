import csv
import math

################################################################################
# Part 1 - Querying the data
################################################################################
def find_bridge_by_id(bridges: list[list], bridge_id: int) -> list:
    """
    从桥梁列表中查找指定ID的桥梁并返回其数据。
    """

    # 1. 遍历bridges列表。
    
    # 2. 对于当前的桥梁，检查其ID是否与我们要查找的bridge_id匹配。
    
    # 3. 如果找到匹配的ID，返回当前的桥梁 注意 是整个桥梁 不是id。
    
    # 4. 如果遍历完所有桥梁都没有找到匹配的ID，返回一个空列表。


def find_bridges_in_radius(bridges: list[list], lat: float, lon: float,
                           radius: int, exclusions: list[int]) -> list[int]:
    """
    返回位于给定经纬度半径内的桥梁的ID。
    """

    # 1. 创建一个空列表来保存在指定半径内的桥梁ID。
    
    # 2. 遍历bridges列表。
    
    # 3. 对于当前桥梁，检查其ID是否在exclusions列表中。
    #    如果在exclusions中，跳过当前桥梁，继续遍历下一个桥梁。
    
    # 4. 如果当前桥梁ID不在exclusions中，计算桥梁的位置(lat, lon)与给定位置(lat, lon)之间的距离。
    #    提示: 可以用calculate_distance来计算距离
    
    # 5. 如果计算出的距离小于或等于给定的半径radius，将当前桥梁的ID添加到在指定半径内的桥梁ID列表中。
    
    # 6. 重复步骤3到5，直到遍历完所有桥梁。
    
    # 7. 返回在指定半径内的桥梁ID列表。


def get_bridge_condition(bridges: list[list], bridge_id: int) -> float:
    """
    返回指定ID的桥梁的最近的BCI分数。
    """

    # 1. 使用find_bridge_by_id函数找到指定ID的桥梁的信息。
    
    # 2. 检查找到的桥梁是否为空。
    #    如果桥梁信息为空或桥梁的BCI分数为空，返回MISSING_BCI。
    
    # 3. 从桥梁的BCI分数列表中获取最近的BCI分数。
    #    提示：您可以假设最近的BCI分数位于列表的最后一个位置。
    
    # 4. 如果找到的BCI分数大于0，返回该分数。
    #    否则，返回MISSING_BCI。


def calculate_average_condition(bridge: list, start: int, stop: int) -> float:
    """
    返回在指定开始和结束年份之间的桥梁的平均BCI分数。
    """

    # 1. 从桥梁数据中提取BCI年份和BCI分数列表。
    # hit : years = bridge[COLUMN_BCI][INDEX_BCI_YEARS]
    #       scores = bridge[COLUMN_BCI][INDEX_BCI_SCORES]

    # 2. 初始化总分和计数器为0。这些将用于计算BCI分数的平均值。

    # 3. 使用循环遍历BCI年份列表。
    #    对于每一年，检查该年份是否在指定的开始和结束年份之间。
    
    # 4. 如果当前年份在指定的范围内，再检查该年份的BCI分数是否不等于MISSING_BCI。
    #    如果BCI分数是有效的，将其加到总分上，并将计数器加1。
    
    # 5. 循环结束后，如果计数器大于0，计算BCI分数的平均值并返回。
    #    否则，返回0.0。


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

    # 1. 使用循环遍历桥梁数据列表。
    #   对于每个桥梁,检查其ID是否与指定的bridge_id匹配。
    
    # 2. 如果找到匹配的桥梁ID,更新该桥梁的最后检查日期为inspect_date。
    
    # 3. 从inspect_date中提取年份,并将这个年份插入到该桥梁的BCI年份列表的开头。
    
    # 4. 同样地,将inspect_bci插入到该桥梁的BCI分数列表的开头。
    


def rehabilitate_bridge(bridges: list[list], bridge_ids: list[int],
                        new_year: str, is_major: bool) -> None:
     """
    更新在bridge_ids中指定ID的桥梁的最后修复日期。

    :param bridges: 桥梁数据的列表，每个桥梁的数据也是一个列表。
    :param bridge_ids: 需要更新的桥梁的ID列表。
    :param new_year: 新的修复日期。
    :param is_major: True:则更新主要修复日期 False:更新次要修复日期。
    """
    #1. 使用循环遍历桥梁数据列表。
    #   对于每个桥梁,检查其ID是否在bridge_ids中。
    
    #2. 如果找到匹配的桥梁ID,根据is_major的值决定更新哪个修复日期。
    #   - 如果is_major为True,则更新主要修复日期为new_year。
    #                     bridge[COLUMN_LAST_MAJOR_REHAB]
    #   - 如果is_major为False,则更新次要修复日期为new_year。
    #                      bridge[COLUMN_LAST_MINOR_REHAB] = new_year
    
                


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
    #1. 初始设置第一个桥梁ID为当前最差的桥梁,并获取其BCI分数。
    #                     worst_id = bridge_ids[0]
    #                      worst_bci = ......
    #   这样可以确保在遍历其余的桥梁时始终有一个最差的桥梁和其BCI分数可供比较。

    # 2. 使用循环遍历bridge_ids中的其余桥梁ID。
    #   对于每个ID,使用`get_bridge_condition`函数获取其最新的BCI分数。
    
    #3. 比较当前桥梁的BCI分数与已知的最差BCI分数。
    #                    if bci < worst_bci:
    #   如果当前桥梁的BCI分数更低,更新最差的桥梁ID和其BCI分数。

    #4. 循环结束后,返回已知的最差的桥梁ID。


def map_route(bridges: list[list], lat: float, lon: float,
              max_bridges: int, radius: int) -> list[int]:
    """
    根据给定的起始位置、桥梁列表、最大桥梁数和半径，为桥梁绘制一条路径。

    Parameters:
    - bridges: 桥梁的列表。
    - lat: 起始纬度。
    - lon: 起始经度。
    - max_bridges: 路径上的最大桥梁数量。
    - radius: 查找桥梁的半径。

    Returns:
    - route: 桥梁ID的列表,表示要遍历的路径。
    """

    # 1. 初始化一个空的路径列表，用于存放已选择的桥梁ID
    # route = []

    # 2. 使用给定的纬度、经度和半径，在未访问的桥梁中查找当前位置半径内的桥梁
    # bridge_in_radius = ...

    # 3. 创建一个while循环，只要路径上的桥梁数少于max_bridges并且仍然可以找到桥梁，就继续执行循环

        # 4. 在当前半径内的桥梁中，找到BCI分数最低的桥梁ID
        # next_bridge_id = ...

        # 5. 将该桥梁ID添加到路径列表中
        # route.append(...)

        # 6. 使用桥梁ID查找具体的桥梁信息，以获取其位置
        # next_bridge = ...

        # 7. 更新当前的纬度和经度为选择的桥梁的位置
        # lat, lon = ...

        # 8. 再次查找新位置的半径内的桥梁
        # bridge_in_radius = ...

    # 9. 返回路径列表
    # return route

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

    # 1. 创建一个空列表。
    
    # 2. 你需要查找格式为"(n)=m;"的子字符串,其中n是跨度的编号,m是跨度的长度。
    # hit:所有的m都在 ‘=’ 和 ‘；’中间
    
    # 3. 对于每个找到的 跨度的长度 数据，提取出跨度的长度并将其转换为float。
    
    # 4. 将提取出的浮点数添加到步骤1中创建的列表中。
    
    # 5. 返回列表。
    


def clean_bci_data(bci_years: list[str], start_year: int, bci_scores: list) -> \
        None:
    """
    这个也很简单 year里填start year 然后递减 scores里填将''替换为MISSING_BCI
    """
    

#恭喜你写完了 现在请来加我微信我想扩列：1224917119
# LeetCode

---

> - ☁ 轻松
> - ★ 做出来了但没有题解思路好
> - ☪ 思考很久
> - ⚡ 没有做出✘

| 类型      | 难度☁★☪⚡  | 编号 | 名称
| -        | -          | -   | -
| **链表**
||★| 19 | 删除链表的倒数第N个节点
||☁| 21 | 合并两个有序链表
||★| 23 | 合并K个排序链表
||☁| 24 | 两两交换链表节点
||☁| 25 | K个一组翻转链表
||
| **树**
||
| **图**
||
| **递归**
||★| 10 | 正则表达式匹配
||⚡| 44 | 通配符匹配
||
| **回溯**
||★| 37 | 解数独
||⚡| 39 | 组合总和
||⚡| 40 | 组合总和 II
||☁| 46 | 全排列
||⚡| 47 | 全排列 II
||
| **dfs/bfs**
||☪| 51 | n-皇后
||☁| 52 | n皇后-ii
||★| 212 | 单词搜索-ii
||☪| 675 | 为高尔夫比赛砍树
||
| **贪心**
||☪| 45 | 跳跃游戏-ii
||⚡| 300 | 最长递增子序列 （动态规划/贪心）
||
| **动态规划**
||☁| 70 | 爬楼梯
||⚡| 198 | 打家劫舍
||⚡| 300 | 最长递增子序列 *（动态规划/贪心）*
||☁| 509 | 斐波那契数
||☁| 746 | 使用最小花费爬楼梯
||⚡| 877 | 石子游戏 *(系列)*
||
| **特殊-不一样**
||☪| 11 | 盛水容器
||⚡| 31 | 下一个排列
||⚡| 41 | 缺失的第一个正数
||☪| 42 | 接雨水
||☁| 48 | 旋转图像
||
| **特殊-模拟**
||⚡| 799 | 香槟塔
||
| **特殊-数学**
||☁| 292 | nim-游戏
||⚡| 877 | 石子游戏 *(系列)*
||
| **系列-数字求和**
||★| 1 | 两数之和
||★| 15 | 三数之和
||★| 16 | 最接近的三数之和
||☁| 18 | 四数之和
||
| **系列-数组查找**
||★| 4 | 从多个数组找中位数
||⚡| 33 | 搜索旋转排序数组
||☁| 34 | 在排序数组中查找元素的第一个和最后一个位置
||☁| 35 | 搜索插入位置
||
| **系列-子串**
||☪| 3 | 无重复最长子串
||⚡| 5 | 最长回文子串
||☪| 28 | 子串匹配
||☪| 30 | 串联所有单词的字串
||
| **系列-成对符号**
||☁| 20 | 有效括号
||⚡| 22 | 括号生成
||☪| 32 | 最长有效括号
||
| **系列-石子游戏**
||⚡| 877 | 石子游戏
||
| **系列-没技术**
||☁| 2 | 两数相加
||☁| 6 | Z字形变换
||☁| 7 | 整数反转
||☁| 8 | 字符串转换整数(atoi)
||☁| 9 | 回文数
||★| 12 | 整数转罗马数字
||☁| 13 | 罗马数字转整数
||☁| 14 | 最长公共前缀
||☁| 17 | 电话号码的字母组合
||☁| 26 | 删除排序数组中的重复项
||☁| 27 | 移除元素
||☁| 29 | 两数相除
||☁| 36 | 有效的数独
||☁| 38 | 外观数列
||☁| 43 | 字符串相乘
||☁| 49 | 字母异位词分组
||☁| 50 | pow-x-n
||☁| 68 | 文本左右对齐
||☁| 162 | 寻找峰值
||☁| 165 | 比较版本号
||☁| 326 | 3-的幂
||☁| 447 | 回旋镖的数量
||☁| 524 | 通过删除字母匹配到字典里最长单词
||☁| 704 | 二分查找
||☁| 725 | 分隔链表
||☁| 831 | 隐藏个人信息
||★| 869 | 重新排序得到2的幂
||★| 902 | 最大为N的数字组合
||☁| 1137 | 第-n-个泰波那契数
||☁| 1221 | 分割平衡字符串
||☁| 1894 | 找到需要补充粉笔的学生编号

---

## 链表

- [19] 删除链表的倒数第N个节点
> 单向链表，只遍历一次，`避免到末尾回不来，考虑双指针`。

- [21] 合并两个有序链表

- [23] 合并K个排序链表
> 分治+递归，代码更简洁。

- [24] 两两交换链表节点

- [25] K个一组翻转链表

---

## 树

---

## 图

---

## 递归

- [10] 正则表达式匹配
> 递归方式，代码更简洁。递归思维。

- [44] 通配符匹配
> 递归超时 \
> 题解：\
> 方法1：动态规划\
> 方法2：贪心

---

## 回溯

- [37] 解数独
> 大量分支，`回溯法`。 \
> 题解的代码更加精简。

- [39] 组合总和
> 回溯法， \
> 从局部考虑去回溯很困难解决细枝末节， \
> 从大局观考虑，递归查找，思维和代码更简洁。

- [40] 组合总和 II
> 同上，但需要更巧的剪枝，观察规律，剪掉兄弟结点的枝。

- [46] 全排列
> 将元素插入到空隙。\
> （大多数人使用回溯的方法，本题我这样也没问题。\
> 只是插空的方法，下一题就无法基于本题的方法了。）

- [47] 全排列 II
> 继续按照插空的到的结果，再集中取重，尽管通过了，但显然不"算法"。\
> 题解：回溯 + 剪枝 \
> 巧妙的剪枝，有效去重。

---

## 深度/广度优先

- [51] n-皇后
> 搜索回溯\
> dfs搜索，for回溯。

- [52] n皇后-ii
> 同51题。

- [212] 单词搜索-ii
> 关键在与选择dfs还是bfs，\
> 利用for循环递归调用dfs，加上前后配上vis，\
> 可以实现分支路口的回溯。
>
> 题解使用的`前缀树`方法更加简洁和高效。

- [675] 为高尔夫比赛砍树

---

## 贪心

- [45] 跳跃游戏-ii
> 动态规划 \
> 题解：贪心，时间和空间复杂度都更小。

- [300] 最长递增子序列 （动态规划/贪心）
> 贪心\
> 题解：需要维护一个贪心的列表，才能处理新子序列。

---

## 动态规划

- [70] 爬楼梯
> 同509题

- [198] 打家劫舍
> 动态规划

- [300] 最长递增子序列 （动态规划/贪心）
> 动态规划\
> 题解：关键在于找到状态转移方程。

- [509] 斐波那契数
> 动态规划，入门题

- [746] 使用最小花费爬楼梯
> 动态规划

---

## 特殊

### 不一样

- [11] 盛水容器
> 观察情况，控制变量，`使其单调变化`，可将O(n^2)转为O(n)，避免遗漏一些情况。

- [31] 下一个排列
> 找规律，观察下一个排列与此的变化过程。

- [41] 缺失的第一个正数
> 在常数空间复杂度要求下，需要特殊巧妙的方法， \
> 复用原来的数组空间，利用特殊标记（如负号）进行标记。

- [42] 接雨水
> 顺序扫描，记录最高点，当前点往前回滚到最高点为止，这个区间的闸门都可以去除。（由于需要回滚，时间复杂度最差为O(n^2)） \
> 题解： \
> 方法1：动态规划（有点），两侧各扫描一次，重叠部分。\
> 方法2：双指针，很巧妙，如果能注意到一侧暂时固定，另一侧的水位高度由这侧的高度决定。（与11题异曲同工。）

- [48] 旋转图像
> 找规律

### 模拟

- [799] 香槟塔

### 数学

- [292] nim-游戏
> 博弈问题

- [877] 石子游戏 *(系列)*
> 博弈问题

---

## 系列

### 系列-数字求和

- [1] 两数之和
> 字典 \
> 题解：比较有想法的一点是，插入计算的结果，减少后续判断。同时解决了重复元素判断的问题。

- [15] 三数之和
> `数字类有关大小，都可考虑排序`，利用有序，固定一位，另2位前后向中间移动。

- [16] 最接近的三数之和
> 同上。

- [18] 四数之和
> 同上，以三数之和扩展。

### 系列-数组查找

- [4] 从多个数组找中位数 - 这类有序问题，常常`不需要对所有数都遍历`，取出总共一半的数即可（题解进一步，只需二分法搜索到总计一半的数即可，时间提升至log）。

- [33] 搜索旋转排序数组
> 有一定排序，仍需二分查找，需做更多条件处理。

- [34] 在排序数组中查找元素的第一个和最后一个位置

- [35] 搜索插入位置

### 系列-子串问题

- [3] 无重复最长子串
> dict记录每个字母最后出现的位置，每次整体向前`蠕动`。

- [5] 最长回文子串
> 方法1：利用对称性，`中心扩展法`。 （也可以不加'#'凑奇数） \
> 方法2：动态规划，减少重复的回文判断，但内存消耗大。 \
> 方法3：不推荐专用算法。

- [28] 子串匹配
> KMP。

- [30] 串联所有单词的字串
> 审题后，发现每个词长度相同，滑动窗口处理。

### 系列-成对的符号问题

- [20] 有效括号
> 堆栈。

- [22] 括号生成
> 递归。
> 成对的符号，需要设置左右flag，它们相等时，表示成对。

- [32] 最长有效括号
> 成对的符号，正反的数量不一样，考虑`正反顺序2次遍历`。


### 系列-石子游戏

- [877] 石子游戏
> 方法1：动态规划，思维转换，将两个人的状态，通过改变游戏规则，转为一个状态。 \
> 方法2：数学推理，得出必胜策略。
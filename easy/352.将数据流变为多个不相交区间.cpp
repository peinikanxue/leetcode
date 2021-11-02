/*
 * @lc app=leetcode.cn id=352 lang=cpp
 *
 * [352] 将数据流变为多个不相交区间
 */

#include <iostream>
#include <vector>
#include <map>
using namespace std;

// @lc code=start
class SummaryRanges {
public:
    
    map<int, vector<int>*> interval_dict;

    SummaryRanges() {
    }
    
    void addNum(int val) {
        map<int, vector<int>*>::iterator it_pre = interval_dict.find(val-1);
        map<int, vector<int>*>::iterator it_back = interval_dict.find(val+1);
        if(interval_dict.find(val) != interval_dict.end()){                     // 1.要添加的元素存在
            return; // 存在，不重复添加
        }

        if(it_pre != interval_dict.end() || it_back != interval_dict.end()){    // 2.要添加的元素前后至少存在一个情况
            vector<int> *tmp = nullptr;
            if(it_pre != interval_dict.end()){      // val-1元素存在    // 连接前面部分
                tmp = interval_dict[val-1];
                (*tmp)[1] = val;
            }
            if(it_back != interval_dict.end()){     // val+1元素存在
                if(tmp != nullptr){                 // 连接前后
                    (*tmp)[1] = (*interval_dict[val+1])[1];
                    auto p_back = interval_dict[val+1];
                    delete p_back;                  // 释放掉后面部分申请的空间
                    for(int i=val+1; i <= (*tmp)[1]; ++i){ // 往后遍历，后面属于区间内的重新指向
                        interval_dict[i] = tmp;
                    }
                }else{                              // 连接后面部分
                    tmp = interval_dict[val+1];
                    (*tmp)[0] = val;
                }
            }
            interval_dict[val] = tmp;
        }else{                                                                  // 3.要添加的元素和前后元素都不存在，分配空间添加
            interval_dict[val] = new vector<int>{val, val};
        }
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> ans;
        int pre = -1;
        for(auto d : interval_dict){
            if((*d.second)[1] != pre){
                ans.push_back(*d.second);
                pre = (*d.second)[1];
            }
        }
        return ans;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(val);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */
// @lc code=end

int main(int argc, char const *argv[])
{
    SummaryRanges* obj = new SummaryRanges();
    obj->addNum(1);
    obj->getIntervals();
    obj->addNum(3);
    obj->getIntervals();
    obj->addNum(7);
    obj->getIntervals();
    obj->addNum(2);
    obj->getIntervals();
    obj->addNum(6);
    obj->getIntervals();
    obj->addNum(9);
    obj->getIntervals();
    obj->addNum(10);
    obj->getIntervals();
    obj->addNum(5);
    obj->getIntervals();
    obj->addNum(11);
    obj->getIntervals();
    obj->addNum(8);
    obj->getIntervals();

    for(auto d : obj->interval_dict){
        cout << d.first << " " << (*d.second)[0] << " " << (*d.second)[1] << endl;
    }

    return 0;
}

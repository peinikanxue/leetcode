/*
 * @lc app=leetcode.cn id=211 lang=cpp
 *
 * [211] 添加与搜索单词 - 数据结构设计
 */

#include <iostream>
#include <string>
#include <map>

using namespace std;

// @lc code=start
struct Node{
    map<char, Node*> dict;
    bool is_endpoint;
};

class WordDictionary {
public:
    Node root;
    WordDictionary() {
    }
    
    void addWord(string word) {
        Node* tmp = &root;
        for(int i=0; i<word.length(); ++i){
            char c = word[i];
            auto search = tmp->dict.find(c);
            if(search == tmp->dict.end()){    // 添加新元素
                tmp->dict.emplace(c, new Node());
            }
            // 往下查找
            tmp = tmp->dict[c];
            if(i == word.length()-1)
                tmp->is_endpoint = true;
        }
    }
    
    bool search(string word) {
        return search_sub(word, 0, &root);
    }

    bool search_sub(string word, int start_pos, Node* p){
        auto c = word[start_pos];
        auto search = p->dict.find(c);
        if(search != p->dict.end()){
            if(start_pos == word.length()-1 && p->dict[c]->is_endpoint) // 字母匹配到最后一个，判断是否is_endpoint
                return true;
            else
                return search_sub(word, start_pos+1, p->dict[c]);   // 字母匹配
        }
        else if(c == '.' && !p->dict.empty()){
            if(start_pos == word.length()-1)    // 以'.'结尾，需要遍历这一级所有结点是否有is_endpoint=true
                for(auto sub_node: p->dict)
                    if(sub_node.second->is_endpoint)
                        return true;
            for(auto sub_node: p->dict){        // 匹配'.'
                if(search_sub(word, start_pos+1, sub_node.second))
                    return true;
            }
        }else
            return false;
        return false;
    }

    void func(){
        auto x = new Node();
        cout << x->is_endpoint << endl;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
// @lc code=end

int main(int argc, char const *argv[])
{
    WordDictionary word_dict;
    word_dict.addWord("bad");
    word_dict.addWord("dad");
    word_dict.addWord("mad");
    word_dict.addWord("dnf");
    word_dict.addWord("apple");
    cout << boolalpha;
    cout << word_dict.search("pad") << endl;
    cout << word_dict.search("bad") << endl;
    cout << word_dict.search(".ad") << endl;
    cout << word_dict.search("b..") << endl;
    cout << word_dict.search("app") << endl;
    cout << word_dict.search("apple") << endl;
    cout << word_dict.search("appl.") << endl;
    cout << word_dict.search("app.e") << endl;
    cout << word_dict.search(".") << endl;
    cout << word_dict.search("ba.") << endl;
    cout << word_dict.search("b.") << endl;
    return 0;
}


/*
13/13 cases passed (144 ms)
Your runtime beats 10.86 % of cpp submissions
Your memory usage beats 19.89 % of cpp submissions (96.1 MB)

time: O(n)
space: O(n)
*/

/*
同208题前缀树。
官方题解使用vector作为结点值的存储，因为字母只有26个。
这样空间开销变大了，但查询和插入都变快了。
*/ 
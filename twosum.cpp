#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;
/*
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        cout << "function1, O(n^2)" << endl;
        for (int i = 0; i <= nums.size()-1; i++)
        {
            for (int j = i+1; j <= nums.size()-1; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
*/
/*
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        cout << "function2, 2hash, O(n)" << endl;
        unordered_map<int, int> m;
        for (int i = 0; i <= nums.size()-1; i++)
        {
            m[nums[i]] = i;
        }
        for (int i = 0; i <= nums.size()-1; i++)
        {
            if (m.find(target-nums[i]) != m.end() && m[target-nums[i]] != i)
            {
                return {i, m[target-nums[i]]};
            }
        }
        return {};
    }
};
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        cout << "function3, 1 hash, O(n)" << endl;
        unordered_map<int, int> m;
        for (int i = 0; i <= nums.size()-1; i++)
        {
            if (m.find(target-nums[i]) != m.end())
            {
                return {m[target-nums[i]],i};
            }
            m[nums[i]] = i;
        }
        return {};
    }
};




int main()
{
    
    Solution a;
    vector<int> input;
    input.push_back(2);
    input.push_back(7);
    input.push_back(11);
    input.push_back(15);

    int target = 9;
    vector<int> output = a.twoSum(input, target);
    vector<int>::iterator iter = output.begin();
    for(; iter != output.end(); iter++)
    {
        cout << *iter << endl;
    }
    

    /*
    unordered_map<int, int> m;
    m.insert(make_pair<int,int>(3,0));
    m.insert(make_pair<int,int>(3,1));

    unordered_map<int,int>::const_iterator iter = m.begin();
    for(; iter != m.end(); iter++)
    {
        cout << iter->first << "->" << iter->second << endl;        
    }
    */
    
    return 0;
}

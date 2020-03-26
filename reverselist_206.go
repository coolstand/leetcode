package main

import (
	"fmt"
)
/**
 * Definition for singly-linked list.
 */
type ListNode struct {
    Val int
    Next *ListNode
}
 
func reverseList(head *ListNode) *ListNode {
	var cur *ListNode
	var prev *ListNode
	cur = head
	for cur != nil {
		cur.Next, prev, cur = prev, cur, cur.Next
	}
	return prev
}


func main() {
	node4 := &ListNode{Val:5, Next:nil}
	node3 := &ListNode{Val:4, Next:node4}
	node2 := &ListNode{Val:3, Next:node3}
	node1 := &ListNode{Val:2, Next:node2}
	node := &ListNode{Val:1, Next:node1}
	result := reverseList(node)
	for result != nil {
		fmt.Printf("%v\n", result.Val)
		result = result.Next
	}
	
}
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


func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	dummyHead := &ListNode{Val:0}
	cur := dummyHead
	carry := 0
	for l1 != nil || l2 != nil {
		x := 0
		y := 0
		if l1 != nil { x = l1.Val }
		if l2 != nil { y = l2.Val }
		sum := x + y + carry
		carry = sum / 10
		cur.Next = &ListNode{Val: sum % 10}
		cur = cur.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	if carry > 0 {
		cur.Next = &ListNode{Val: 1}
	}
		
	return dummyHead.Next
}

func main() {
	/*
	node2 := &ListNode{Val:3, Next:nil}
	node1 := &ListNode{Val:4, Next:node2}
	node := &ListNode{Val:2, Next:node1}

	node5 := &ListNode{Val:4, Next:nil}
	node4 := &ListNode{Val:6, Next:node5}
	node3 := &ListNode{Val:5, Next:node4}
	*/
	node1 := &ListNode{Val:8, Next:nil}
	node := &ListNode{Val:1, Next:node1}

	node3 := &ListNode{Val:0, Next:nil}
	result := addTwoNumbers(node, node3)
	for result != nil {
		fmt.Printf("%v\n", result.Val)
		result = result.Next
	}



}
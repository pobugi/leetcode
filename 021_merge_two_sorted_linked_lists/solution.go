package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	result := &ListNode{}
	curr := result
	curr1 := list1
	curr2 := list2

	for curr1 != nil && curr2 != nil {
		if curr1.Val > curr2.Val {
			curr.Next = curr2
			curr2 = curr2.Next
		} else {
			curr.Next = curr1
			curr1 = curr1.Next
		}
		curr = curr.Next
	}
	if curr1 != nil {
		curr.Next = curr1
	}
	if curr2 != nil {
		curr.Next = curr2
	}
	return result.Next
}

func main() {
	node1 := ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4}}}
	node2 := ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4}}}

	fmt.Println(mergeTwoLists(&node1, &node2))
}

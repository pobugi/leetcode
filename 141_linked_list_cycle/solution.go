package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	var fast = head
	var slow = head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false
}

func main() {
	mon := ListNode{Val: 1}
	tue := ListNode{Val: 2}
	wed := ListNode{Val: 3}
	thu := ListNode{Val: 4}
	fri := ListNode{Val: 5}
	sat := ListNode{Val: 6}
	sun := ListNode{Val: 7}

	mon.Next = &tue
	tue.Next = &wed
	wed.Next = &thu
	thu.Next = &fri
	fri.Next = &sat
	sat.Next = &sun
	sun.Next = &mon

	fmt.Println(hasCycle(&mon))
}

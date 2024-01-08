#include "lists.h"

listint_t *reverse_list(listint_t *head);
int compare_lists(listint_t *list1, listint_t *list2);


/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *mid_node;
	listint_t *prev_slow = *head;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);


	slow = *head;
	fast = *head;


	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}


	second_half = reverse_list(slow);


	result = compare_lists(*head, second_half);

	prev_slow->next = reverse_list(second_half);


	if (mid_node != NULL)
		prev_slow->next = mid_node;

	return (result);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

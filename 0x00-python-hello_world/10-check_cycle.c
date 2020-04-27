#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle
 *
 * @list: Linked list
 *
 * Return: If the linked list has a cycle, 1
 * if not, 0
 **/
int check_cycle(listint_t *list)
{
	listint_t *s_slow, *s_fast;

	s_slow = s_fast = list;
	while (s_slow != NULL && s_fast != NULL && s_fast->next != NULL)
	{
		s_slow = s_slow->next;
		s_fast = s_fast->next->next;

		if (s_slow == s_fast)
			return (1);
	}

	return (0);
}

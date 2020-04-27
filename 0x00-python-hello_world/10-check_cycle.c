#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *s_low, *s_fast;

	s_low = s_fast = list;
	s_fast = s_fast->next;

	while(s_low != NULL && s_fast->next != NULL)
	{
		if (s_low->n == s_fast->n)
			return (1);

		s_low = s_low->next;
		s_fast = s_fast->next->next;
	}

	return (0);
}

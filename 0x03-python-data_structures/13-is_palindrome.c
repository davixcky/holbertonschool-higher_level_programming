#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	int size;
	int *options;
	int i;

	size = 0;
	if (head == NULL || *head == NULL)
		return (1);

	options = malloc(sizeof(int));
	while(*head != NULL)
	{
		size++;
		options = realloc(options, sizeof(int) * size);
		options[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (options[i] != options[size - i - 1])
			return (0);
	}

	return (1);
}

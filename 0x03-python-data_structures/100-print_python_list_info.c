#include <python.h>

/**
 * print_python_list_info - prints python list
 * @p: the py object
 * Return: void
*/
void print_python_list_info(PyObject *p)
{

	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t allocated = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);

		printf("[*] Address of the PyObject = %p\n", (void *)p);

		for (Py_ssize_t i = 0; i < size; ++i)
		{
			printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "Invalid Python List\n");
	}
}

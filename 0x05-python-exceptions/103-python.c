#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: A PyObject bytes object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;
fflush(stdout);
printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
str = PyBytes_AsString(p);
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);
printf("  first 10 bytes: ");
for (i = 0; i < size && i < 10; i++)
printf("%02x ", (unsigned char)str[i]);
printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
fflush(stdout);
printf("[.] float object info\n");
if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

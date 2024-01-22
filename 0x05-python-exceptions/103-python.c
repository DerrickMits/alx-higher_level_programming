#include <Python.h>
#include <floatobject.h>
#include <object.h>
#include <bytesobject.h>
#include <listobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;
Py_ssize_t i, size;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", var->ob_size);
printf("[*] Allocated = %ld\n", var->ob_alloc);
for (i = 0, size = var->ob_size; i < size; ++i) {
PyObject *item = list->ob_item[i];
printf("Element %ld: %s\n", i, item->ob_type->tp_name);

if (PyBytes_Check(item))
{
print_python_bytes(item);
}
else if (PyFloat_Check(item))
{
print_python_float(item);
}
}
}

void print_python_bytes(PyObject *p) {
PyBytesObject *bytes = (PyBytesObject *)p;
PyVarObject *var = (PyVarObject *)p;
Py_ssize_t i, size;
char *str;
printf("[.] bytes object info\n");
printf("  size: %ld\n", var->ob_size);
printf("  trying string: %s\n", PyUnicode_AsUTF8(PyObject_Str(p)));
printf("  first %ld bytes: ", var->ob_size < 10 ? var->ob_size : 10);
str = PyBytes_AsString(p);
for (i = 0, size = var->ob_size < 10 ? var->ob_size : 10; i < size; ++i)
{
printf("%02hhx ", str[i]);
}
printf("\n");
}

void print_python_float(PyObject *p) {
PyFloatObject *float_obj = (PyFloatObject *)p;
printf("[.] float object info\n");
printf("  value: %f\n", float_obj->ob_fval);
}

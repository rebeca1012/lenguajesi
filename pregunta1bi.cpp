/*
Alumno: Rebeca Ledesma
Carné: 15-10771
Lenguajes de Programación I
Tarea 3
Pregunta 1.b.i
*/
#include <iostream>
#include <queue>
#include <stack>
#include <stdexcept>

using namespace std;

// Interfaz Secuencia
template <typename T>
class Secuencia {
public:
    virtual void agregar(const T& elemento) = 0;
    virtual T remover() = 0;
    virtual bool vacio() const = 0;
    virtual ~Secuencia() {}
};

// Clase Pila
template <typename T>
class Pila : public Secuencia<T> {
private:
    stack<T> pila;
public:
    void agregar(const T& elemento) override {
        pila.push(elemento);
    }

    T remover() override {
        if (pila.empty()) {
            throw runtime_error("La pila está vacía");
        }
        T elemento = pila.top();
        pila.pop();
        return elemento;
    }

    bool vacio() const override {
        return pila.empty();
    }
};

// Clase Cola
template <typename T>
class Cola : public Secuencia<T> {
private:
    queue<T> cola;
public:
    void agregar(const T& elemento) override {
        cola.push(elemento);
    }

    T remover() override {
        if (cola.empty()) {
            throw runtime_error("La cola está vacía");
        }
        T elemento = cola.front();
        cola.pop();
        return elemento;
    }

    bool vacio() const override {
        return cola.empty();
    }
};

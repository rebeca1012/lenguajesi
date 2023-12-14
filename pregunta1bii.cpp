/*
Alumno: Rebeca Ledesma
Carné: 15-10771
Lenguajes de Programación I
Tarea 3
Pregunta 1.b.ii BFS y DFS
*/

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>

using namespace std;
// Tipo de datos para representar grafos como listas de adyacencias
using Grafo = unordered_map<int, vector<int>>;

// Clase abstracta Busqueda
class Busqueda {
public:
    virtual int buscar(int D, int H, const Grafo& grafo) = 0;
    virtual ~Busqueda() {}
};

// Clase concreta DFS
class DFS : public Busqueda {
public:
    int buscar(int D, int H, const Grafo& grafo) override {
        unordered_map<int, bool> visitado;
        stack<int> pila;
        int nodosExplorados = 0;

        pila.push(D);
        while (!pila.empty()) {
            int nodo = pila.top();
            pila.pop();

            if (visitado[nodo]) continue;
            visitado[nodo] = true;
            nodosExplorados++;

            if (nodo == H) return nodosExplorados;

            for (int vecino : grafo.at(nodo)) {
                if (!visitado[vecino]) {
                    pila.push(vecino);
                }
            }
        }

        return -1;  // H no es alcanzable desde D
    }
};

// Clase concreta BFS
class BFS : public Busqueda {
public:
    int buscar(int D, int H, const Grafo& grafo) override {
        unordered_map<int, bool> visitado;
        queue<int> cola;
        int nodosExplorados = 0;

        cola.push(D);
        while (!cola.empty()) {
            int nodo = cola.front();
            cola.pop();

            if (visitado[nodo]) continue;
            visitado[nodo] = true;
            nodosExplorados++;

            if (nodo == H) return nodosExplorados;

            for (int vecino : grafo.at(nodo)) {
                if (!visitado[vecino]) {
                    cola.push(vecino);
                }
            }
        }

        return -1;  // H no es alcanzable desde D
    }
};

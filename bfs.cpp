// Program to print BFS traversal from a given
// source vertex. BFS(int s) traverses vertices
// reachable from s.
#include <iostream>
#include <list>
#include <vector>
#include <string>

using namespace std;

// This class represents a directed graph using
// adjacency list representation
class Graph
{
    int V;    // No. of vertices

    // Pointer to an array containing adjacency
    // lists
    list<int> *adj;
public:
    Graph(int V);  // Constructor

    // function to add an edge to graph
    void addEdge(int v, int w);

    // prints BFS traversal from a given source s
    void BFS(int s);
};

Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w); // Add w to v’s list.
}

void Graph::BFS(int s)
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for(int i = 0; i < V; i++)
        visited[i] = false;

    // Create a queue for BFS
    list<int> queue;

    // Mark the current node as visited and enqueue it
    visited[s] = true;
    queue.push_back(s);

    // 'i' will be used to get all adjacent
    // vertices of a vertex
    list<int>::iterator i;

    while(!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        // Get all adjacent vertices of the dequeued
        // vertex s. If a adjacent has not been visited,
        // then mark it visited and enqueue it
        for (i = adj[s].begin(); i != adj[s].end(); ++i)
        {
            if (!visited[*i])
            {
                visited[*i] = true;
                queue.push_back(*i);
            }
        }
    }
}

int height = 4;
int width = 7;
char board[4][7] = {
  {'O','O','O','O','X','X','O'},
  {'O','X','O','X','O','O','X'},
  {'X','X','X','X','O','X','O'},
  {'O','X','X','X','O','O','O'}
};
struct coord {
  int x;
  int y;
};
struct edge {
  int a;
  int b;
};
int main() {
  int V = 4 * 7;
  vector<coord> coords;
  vector<edge> edges;
  for (size_t x = 0; x < height; x++) {
    for (size_t y = 0; y < width; y++) {
      char a = board[x][y];
      if (a == 'X') {
        coord a = {x, y};
        int A = x * width + y;
        // Look left
        if (x > 0) {
          if (board[x - 1][y] == 'X') {
            coord b = {x - 1, y};
            int B = (x - 1) * width + y;
            edge e = {A, B};
            edges.push_back(e);
          }
        }
        // Look right
        if (x < height) {
          if (board[x + 1][y] == 'X') {
            coord b = {x + 1, y};
            int B = (x + 1) * width + y;
            edge e = {A, B};
            edges.push_back(e);
          }
        }
        // Look down
        if (y > 0) {
          if (board[x][y - 1] == 'X') {
            coord b = {x, y - 1};
            int B = (x) * width + (y - 1);
            edge e = {A, B};
            edges.push_back(e);
          }
        }
        // Look up
        if (y < width) {
          if (board[x][y + 1] == 'X') {
            coord b = {x, y + 1};
            int B = (x) * width + (y + 1);
            edge e = {A, B};
            edges.push_back(e);
          }
        }
      }
    }
  }

  Graph g(V);
  for (size_t i = 0; i < edges.size(); i++) {
    // cout << edges[i].a << " " << edges[i].b << endl;
    g.addEdge(edges[i].a, edges[i].b);
    // cout << "(" << edges[i].a.x << ", " << edges[i].a.y << ") -> (" <<
    // edges[i].b.x << ", " << edges[i].b.y << ")" << endl;
  }
  for (size_t i = 0; i < 4 * 7; i++) {
    g.BFS(i);
    cout << endl;
  }
  // g.addEdge(0, 1);
  return 0;
  // cout << V;
}
// int main() {
//   int num_trials;
//   for (size_t i = 0; i < num_trials; i++) {
//     int n, m;
//     cin >> n >> m;
//     for (size_t j = 0; j < n; j++) {
//       for (size_t k = 0; k < m; k++) {
//         char a;
//         cin >> a;
//         cout << a;
//       }
//     }
//   }
// }

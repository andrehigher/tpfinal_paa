#include <iostream>
#include <cassert>
#include <cstdio>
#include <algorithm>
using namespace std;

#define maxn 1000000
#define maxv 1000 + 5

int n, m, x[maxn], y[maxn], z[maxn], i, source, dest, gx_nodes, c[maxv], gx_a[maxv][maxv], my_wei, node, cn, e[maxv][maxv], ew[maxv][maxv], e0[maxv], j, k, minwei[maxv], q1, q2, queue[maxv], was[maxv], iteration, ret = 1;
bool interest[maxv], cl[maxv];

namespace dinic {
    int ii, f[maxn], t[maxn], p[maxn], i, q1, q2, was[maxn], iteration, last[maxn];
    int queue[maxn], min_weight[maxn], k, q, fl[maxn], pr[maxn], o[maxn], depth[maxn], oe[maxn];

    void addedge (int x, int y, int z) {
        t[++ii] = y; p[ii] = f[x]; f[x] = ii; fl[ii] = z; o[ii] = ii + 1;
        t[++ii] = x; p[ii] = f[y]; f[y] = ii; fl[ii] = 0; o[ii] = ii - 1;
    }

    void clear () {
        ii = 0;
        for(i = 1; i <= n; i++) f[i] = 0;
    }

    bool bfs (int k) {
        q1 = q2 = 0;
        queue[q1++] = k;
        depth[k] = 0;
        was[k] = ++iteration;
        while (q1 != q2) {
            k = queue[q2++];
            q = f[k];
            while (q > 0) {
                if (was[t[q]] != iteration && fl[q]) {
                    was[t[q]] = iteration;
                    queue[q1++] = t[q];
                    depth[t[q]] = 1 + depth[k];
                }
                q = p[q];
            }
        }
        return was[dest] == iteration;
    }

    int dfs (int k, int flow) {
        if (!flow || k == dest) return flow;
        int to, pushed;
        while (last[k] > 0) {
            if (depth[t[last[k]]] > depth[k] && fl[last[k]]) {
                to = t[last[k]];
                pushed = dfs(to, min(flow, fl[last[k]]));
                if (pushed) {
                    fl[last[k]] -= pushed;
                    fl[o[last[k]]] += pushed;
                    last[k] = p[last[k]];
                    return pushed;
                }
                last[k] = p[last[k]];
            } else last[k] = p[last[k]];
        }
        return 0;
    }

    int maximal_flow (int from, int dest) {
        int ret = 0;
        while (true) {
            for(i = 1; i <= n; i++) last[i] = f[i];
            if (!bfs(from)) break;
            while (int pushed = dfs(from, 1000000000)) ret += pushed;
        }
        return ret;
    }

    void get_cut (int k) {
        q1 = q2 = 0;
        was[k] = ++iteration;
        queue[q1++] = k;
        while (q1 != q2) {
            k = queue[q2++];
            q = f[k];
            while (q > 0) {
                if (was[t[q]] != iteration && fl[q] > 0 && o[q] == q + 1) {
                    queue[q1++] = t[q];
                    was[t[q]] = iteration;
                }
                q = p[q];
            }
        }
        for(i = 1; i <= n; i++) cl[i] = 0;
        for(i = 0; i < q1; i++) cl[queue[i]] = 1;
    }
}

void get_min_cut (int node) {
    dinic::clear();
    for(i = 1; i <= n; i++) interest[i] = false;
    for(i = 1; i <= c[node]; i++) interest[gx_a[node][i]] = true;
    for(i = 1; i <= m; i++)/* if (interest[x[i]] && interest[y[i]]) */{
        dinic::addedge(x[i], y[i], z[i]);
        dinic::addedge(y[i], x[i], z[i]);
    }
    my_wei = dinic::maximal_flow(source, dest);
    dinic::get_cut(source);
}

int main (int argc, char * const argv[]) {
//    freopen("input.txt", "r", stdin);
    scanf("%d %d", &n, &m);
    for(i = 1; i <= m; i++) scanf("%d %d %d", &x[i], &y[i], &z[i]);
    gx_nodes = 1; c[1] = n;
    for(i = 1; i <= n; i++) gx_a[1][i] = i;
    while (gx_nodes != n) {
        for(i = 1; i <= gx_nodes; i++) if (c[i] > 1) {
            source = gx_a[i][1];
            dest = gx_a[i][2];
            node = i;
            break;
        }
        get_min_cut(node);
        cn = 0;
        for(i = 1; i <= c[node]; i++) if (!cl[gx_a[node][i]]) gx_a[gx_nodes + 1][++c[gx_nodes + 1]] = gx_a[node][i]; else gx_a[node][++cn] = gx_a[node][i];
        c[node] = cn;
        e[node][++e0[node]] = gx_nodes + 1;
        ew[node][e0[node]] = my_wei;
        e[gx_nodes + 1][++e0[gx_nodes + 1]] = node;
        ew[gx_nodes + 1][e0[gx_nodes + 1]] = my_wei;
        ++gx_nodes;
    }
    for(i = 1; i <= n; i++) {
        q1 = q2 = 0;
        queue[q1++] = i;
        was[i] = ++iteration;
        minwei[i] = 1000000000;
        while (q1 != q2) {
            k = queue[q2++];
            for(j = 1; j <= e0[k]; j++) if (was[e[k][j]] != iteration) {
                was[e[k][j]] = iteration;
                minwei[e[k][j]] = min(minwei[k], ew[k][j]);
                queue[q1++] = e[k][j];
            }
        }
        for(j = i + 1; j <= n; j++) {
            ret = (ret * 1LL * minwei[j]) % 1000000007;
            assert(was[j] == iteration);
        }
    }
    printf("%d\n", ret);
    return 0;
}

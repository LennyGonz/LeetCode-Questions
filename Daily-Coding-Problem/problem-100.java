// X and Y co-ordinates of the points in order.
// Each point is represented by (X.get(i), Y.get(i))
public int coverPoints(ArrayList<Integer> X, ArrayList<Integer> Y) {
    int totalDistance = 0;
    for (int i = 1; i < X.size(); i++) {
        totalDistance += getDistance(X.get(i - 1), Y.get(i - 1), X.get(i), Y.get(i));
    }
    return totalDistance;
}

private int getDistance(int x1, int y1, int x2, int y2) {
    return (int)Math.max(Math.abs(x2 - x1), Math.abs(y2 - y1));
}

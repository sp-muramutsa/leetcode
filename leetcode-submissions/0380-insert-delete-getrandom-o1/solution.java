class RandomizedSet {
    Map<Integer, Integer> dic;
    List<Integer> list;
    Random rand = new Random();

    public RandomizedSet() {
        dic = new HashMap();
        list = new ArrayList();
    }
    
    public boolean insert(int val) {
        if (dic.containsKey(val)) {
            return false;
        } 

        dic.put(val, list.size());
        list.add(list.size(), val);
        return true;
    }
    
    public boolean remove(int val) {

        if (!dic.containsKey(val)) {
            return false;
        }

        int lastElement = list.get(list.size() - 1);
        int idx = dic.get(val);
        list.set(idx, lastElement);
        dic.put(lastElement, idx);

        dic.remove(val);
        list.remove(list.size() - 1);
        return true;
    }
    
    public int getRandom() {
        return list.get(rand.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

// 1. Init different data structures
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // 1.1 Init List with input content
        List<string> list1 = new List<string>()
        {
            "carrot",
            "fox",
            "exploer"
        };

        var list2 = new List<string>()
        {
            "carrot",
            "fox",
            "exploer"
        };

        // 1.2 Init List with array as input
        string[] array = {"carrot", "fox", "exploer"};
        List<string> list3 = new List<string>(array);

        // 1.3 Init List with capacity
        List<string> list4 = new List<string>(3);
        list4.Add(null);
        list4.Add(null);
        list4.Add(null);
        list4[0] = "carrot";
        list4[1] = "fox";
        list4[2] = "exploer";

        // 1.4 use Add method with unspecified pre condi
        List<string> list5 = new List<string>();
        list5.Add("carrot");
        list5.Add("fox");
        list5.Add("exploer");


        //  2. Dictionary with Tuple
        public Dictionary<Tuple<string, int>, int> store = new Dictionary<Tuple<string, int>, int>();
    }
}
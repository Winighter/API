import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:kis/screens/future_hoka_screen.dart';
import 'package:kis/screens/balance_screen.dart';
import 'package:kis/screens/screen3.dart';
import 'package:kis/services/common/issue_token.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 1;
  final List<Widget> _navIndex = [
    BalancePage(),
    FutureHokaPage(),
    MyInfoPage(),
  ];

  void _onNavTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  final tokens = postAccessToken('N');

  @override
  Widget build(BuildContext context) {
    bool isTrading = false;
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Colors.black,
          foregroundColor: Colors.white,
          centerTitle: true,
          // title: const Text(
          //   "한국투자증권",
          //   style: TextStyle(fontSize: 24),
          // ),
          actions: [
            CupertinoSwitch(
                value: isTrading,
                activeColor: Colors.grey,
                onChanged: (bool? value) {
                  setState(() {
                    isTrading = value ?? false;
                  });
                })
          ]),
      body: _navIndex.elementAt(_selectedIndex),
      bottomNavigationBar: BottomNavigationBar(
        fixedColor: Colors.blue,
        unselectedItemColor: Colors.blueGrey,
        items: const [
          BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.star_fill),
              label: '메뉴',
              backgroundColor: Colors.white),
          BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.person_alt_circle_fill),
              label: '홈',
              backgroundColor: Colors.white),
          BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.circle_grid_3x3_fill),
              label: '메뉴',
              backgroundColor: Colors.white),
        ],
        currentIndex: _selectedIndex,
        onTap: _onNavTapped,
      ),
    );
  }
}

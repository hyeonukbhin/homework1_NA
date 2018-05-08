#!/usr/bin/python3
#-*- coding: utf-8 -*-

/********************************************************************************
** Form generated from reading UI file 'designerjt3267.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef DESIGNERJT3267_H
#define DESIGNERJT3267_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCommandLinkButton>
#include <QtWidgets/QDateTimeEdit>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QDateTimeEdit *dateTimeEdit;
    QWidget *gridLayoutWidget_3;
    QGridLayout *gridLayout_2;
    QPushButton *pushButton_5;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_13;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QLabel *label_11;
    QLabel *label_14;
    QPushButton *pushButton_8;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_17;
    QLCDNumber *lcdNumber;
    QCommandLinkButton *commandLinkButton;
    QCommandLinkButton *commandLinkButton_2;
    QLabel *label_12;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1137, 875);
        MainWindow->setCursor(QCursor(Qt::PointingHandCursor));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        dateTimeEdit = new QDateTimeEdit(centralwidget);
        dateTimeEdit->setObjectName(QStringLiteral("dateTimeEdit"));
        dateTimeEdit->setGeometry(QRect(805, 426, 241, 31));
        gridLayoutWidget_3 = new QWidget(centralwidget);
        gridLayoutWidget_3->setObjectName(QStringLiteral("gridLayoutWidget_3"));
        gridLayoutWidget_3->setGeometry(QRect(80, 90, 970, 330));
        gridLayout_2 = new QGridLayout(gridLayoutWidget_3);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(10, 10, 10, 10);
        pushButton_5 = new QPushButton(gridLayoutWidget_3);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));

        gridLayout_2->addWidget(pushButton_5, 4, 4, 1, 1);

        label_9 = new QLabel(gridLayoutWidget_3);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setPixmap(QPixmap(QString::fromUtf8(":/pictures/coursework/homework1_NA/vending_machine/assets/images/KoKaCola.jpeg")));
        label_9->setOpenExternalLinks(false);

        gridLayout_2->addWidget(label_9, 1, 0, 1, 1);

        label_10 = new QLabel(gridLayoutWidget_3);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setMaximumSize(QSize(16777215, 16777215));
        label_10->setBaseSize(QSize(0, 0));
        label_10->setLayoutDirection(Qt::LeftToRight);
        label_10->setFrameShape(QFrame::NoFrame);
        label_10->setFrameShadow(QFrame::Plain);
        label_10->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_10, 2, 0, 1, 1);

        label_13 = new QLabel(gridLayoutWidget_3);
        label_13->setObjectName(QStringLiteral("label_13"));
        label_13->setPixmap(QPixmap(QString::fromUtf8(":/pictures/coursework/homework1_NA/vending_machine/assets/images/Water.jpeg")));
        label_13->setOpenExternalLinks(false);

        gridLayout_2->addWidget(label_13, 1, 4, 1, 1);

        pushButton_6 = new QPushButton(gridLayoutWidget_3);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));

        gridLayout_2->addWidget(pushButton_6, 4, 0, 1, 1);

        pushButton_7 = new QPushButton(gridLayoutWidget_3);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));

        gridLayout_2->addWidget(pushButton_7, 4, 2, 1, 1);

        label_11 = new QLabel(gridLayoutWidget_3);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setPixmap(QPixmap(QString::fromUtf8(":/pictures/coursework/homework1_NA/vending_machine/assets/images/Pepchi.jpeg")));
        label_11->setOpenExternalLinks(false);

        gridLayout_2->addWidget(label_11, 1, 2, 1, 1);

        label_14 = new QLabel(gridLayoutWidget_3);
        label_14->setObjectName(QStringLiteral("label_14"));
        label_14->setPixmap(QPixmap(QString::fromUtf8(":/pictures/coursework/homework1_NA/vending_machine/assets/images/Starblues.jpeg")));
        label_14->setOpenExternalLinks(false);

        gridLayout_2->addWidget(label_14, 1, 3, 1, 1);

        pushButton_8 = new QPushButton(gridLayoutWidget_3);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));

        gridLayout_2->addWidget(pushButton_8, 4, 3, 1, 1);

        label_15 = new QLabel(gridLayoutWidget_3);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setMaximumSize(QSize(16777215, 16777215));
        label_15->setBaseSize(QSize(0, 0));
        label_15->setLayoutDirection(Qt::LeftToRight);
        label_15->setFrameShape(QFrame::NoFrame);
        label_15->setFrameShadow(QFrame::Plain);
        label_15->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_15, 2, 2, 1, 1);

        label_16 = new QLabel(gridLayoutWidget_3);
        label_16->setObjectName(QStringLiteral("label_16"));
        label_16->setMaximumSize(QSize(16777215, 16777215));
        label_16->setBaseSize(QSize(0, 0));
        label_16->setLayoutDirection(Qt::LeftToRight);
        label_16->setFrameShape(QFrame::NoFrame);
        label_16->setFrameShadow(QFrame::Plain);
        label_16->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_16, 2, 3, 1, 1);

        label_17 = new QLabel(gridLayoutWidget_3);
        label_17->setObjectName(QStringLiteral("label_17"));
        label_17->setMaximumSize(QSize(16777215, 16777215));
        label_17->setBaseSize(QSize(0, 0));
        label_17->setLayoutDirection(Qt::LeftToRight);
        label_17->setFrameShape(QFrame::NoFrame);
        label_17->setFrameShadow(QFrame::Plain);
        label_17->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_17, 2, 4, 1, 1);

        lcdNumber = new QLCDNumber(centralwidget);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));
        lcdNumber->setGeometry(QRect(710, 560, 291, 61));
        lcdNumber->setFrameShape(QFrame::NoFrame);
        lcdNumber->setProperty("intValue", QVariant(150));
        commandLinkButton = new QCommandLinkButton(centralwidget);
        commandLinkButton->setObjectName(QStringLiteral("commandLinkButton"));
        commandLinkButton->setGeometry(QRect(730, 510, 31, 41));
        commandLinkButton_2 = new QCommandLinkButton(centralwidget);
        commandLinkButton_2->setObjectName(QStringLiteral("commandLinkButton_2"));
        commandLinkButton_2->setGeometry(QRect(780, 510, 31, 41));
        label_12 = new QLabel(centralwidget);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(100, 540, 233, 254));
        label_12->setPixmap(QPixmap(QString::fromUtf8(":/pictures/coursework/homework1_NA/vending_machine/assets/images/KoKaCola.jpeg")));
        label_12->setOpenExternalLinks(false);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 1137, 25));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        pushButton_5->setText(QApplication::translate("MainWindow", "O", 0));
        label_9->setText(QString());
        label_10->setText(QApplication::translate("MainWindow", "Pepchi", 0));
        label_13->setText(QString());
        pushButton_6->setText(QApplication::translate("MainWindow", "O", 0));
        pushButton_7->setText(QApplication::translate("MainWindow", "O", 0));
        label_11->setText(QString());
        label_14->setText(QString());
        pushButton_8->setText(QApplication::translate("MainWindow", "O", 0));
        label_15->setText(QApplication::translate("MainWindow", "Pepchi", 0));
        label_16->setText(QApplication::translate("MainWindow", "Pepchi", 0));
        label_17->setText(QApplication::translate("MainWindow", "Pepchi", 0));
        commandLinkButton->setText(QString());
        commandLinkButton_2->setText(QString());
        label_12->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // DESIGNERJT3267_H

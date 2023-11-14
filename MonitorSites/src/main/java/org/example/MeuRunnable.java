package org.example;

public class MeuRunnable implements Runnable {


    @Override
    public void run() {
        System.out.println("Ola Mundo!");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        Thread t = Thread.currentThread();
        System.out.println("Id: " +  t.getId() + " Name: " + t.getName());
    }
}

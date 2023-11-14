package org.example;

import kong.unirest.Unirest;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        String[] sites = {
                "https://g1.globo.com/",
                "https://noticias.uol.com.br/",
                "https://www.r7.com/",
                "https://www.cnnbrasil.com.br/"
        };

        List<Thread> threads = new ArrayList<>();
        for (String site : sites) {
           threads.add(new Thread(() -> monitor(site, 15, 10)));
        }

        for (Thread thread: threads) {
            thread.start();
        }

    }

    public static void monitor(String url, int intervalo, int quantidade) {

        System.out.println(Thread.currentThread().getId());

        String _r = "";
        for (int i = 1; i <= quantidade; i++) {
            System.out.println("Tentativa " +  i + " no site " + url);
            String r = Unirest.get(url).asString().getBody();
            if (!_r.isEmpty() && !r.equals(_r)) {
                System.out.println("O site " + url + " foi modificado na tentativa " + i);
            }
            _r = r;
            try {
                Thread.sleep(intervalo * 1000L);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

}